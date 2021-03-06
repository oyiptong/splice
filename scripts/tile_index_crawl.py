#!/usr/bin/env python

from optparse import OptionParser
import grequests
import requests
import traceback
requests.packages.urllib3.disable_warnings()


def validate(results, verbose, errors):
    for r in results:
        try:
            if r.status_code != 200:
                msg = 'ERROR: %s %s' % (r.url, r.status_code)
                print(msg)
                errors.append(msg)
                continue
            elif verbose:
                print('SUCCESS: %s %s' % (r.url, r.status_code))
            yield r
        except Exception as e:
            msg = 'ERROR: %s' % e
            print(msg)
            print(traceback.format_exc())
            errors.append(msg)


def main():
    # get argument
    parser = OptionParser(
        usage='Usage: %prog [<CDN_URL>]'
        '\n\nArguments:'
        '\n  CDN_URL    Of the format "<scheme>://<fqdn>".'
        ' Trailing "/" not allowed.'
        '\n\nExamples:'
        '\n  %prog https://tiles.cdn.mozilla.net'
    )
    parser.set_defaults(
        quiet=False,
        verbose=False,
    )
    parser.add_option(
        '-q', '--quiet',
        action='store_true',
        dest='quiet',
        help="Don't report NOTICE",
    )
    parser.add_option(
        '-v', '--verbose',
        action='store_true',
        dest='verbose',
        help='Report SUCCESS',
    )
    options, args = parser.parse_args()

    try:
        from splice.environment import Environment
        config = Environment.instance().config
        cdn = 'https://%s.s3.amazonaws.com' % config.S3['bucket']
        tile_index_key = config.S3['tile_index_key']
    except Exception:
        cdn = 'https://tiles.cdn.mozilla.net'
        tile_index_key = 'tile_index_v3.json'

    channels = [
        'desktop',
        'android',
        'desktop-prerelease',
        'hello'
    ]

    if len(args) == 1:
        cdn = args.pop()
    elif len(args) > 1:
        parser.parse_args(['-h'])

    if not options.quiet:
        print(
            'NOTICE: crawling: %s/%s_%s' %
            (cdn, tuple(channels), tile_index_key)
        )
        print('NOTICE: calculating tiles urls')

    errors = []

    # extract tiles urls from tile index
    try:
        urls = [
            tiles_url
            for index in validate(
                grequests.imap(
                    (grequests.get('%s/%s_%s' % (cdn, channel, tile_index_key), allow_redirects=False,)
                     for channel in channels),
                    size=10
                ),
                options.verbose,
                errors,
            )
            for key, value in index.json().iteritems()
            if '/' in key
            for tiles_url in value.values()
        ]

        tiles_urls = set()
        for url in urls:
            if type(url) is list:
                tiles_urls.update(url)
            else:
                tiles_urls.add(url)

        if not options.quiet:
            print('NOTICE: tiles urls extracted: %s' % len(tiles_urls))
            print('NOTICE: calculating image urls')

        # extract image urls from tiles
        image_urls = set([
            image_url
            for tiles in validate(
                grequests.imap(
                    (grequests.get(tiles_url, allow_redirects=False)
                     for tiles_url in tiles_urls),
                    size=10
                ),
                options.verbose,
                errors,
            )
            for value_x in tiles.json().values()
            for value_y in value_x
            for key, image_url in value_y.iteritems()
            if key in ['imageURI', 'enhancedImageURI']
        ])

        if not options.quiet:
            print('NOTICE: image urls extracted: %s' % len(image_urls))
            print('NOTICE: validating image urls')

        # Two things to notice here:
        # 1. expanding the list comprehension is necessary to get the 'validate'
        #    step above to actually evaluate (it's lazy.)
        # 2. the actual value of the list comprehension is dropped, not returned.
        [
            valid.url
            for valid in validate(
                grequests.imap(
                    (grequests.head(image_url, allow_redirects=False)
                     for image_url in image_urls),
                    size=10
                ),
                options.verbose,
                errors,
            )
        ]
    except Exception as e:
        msg = 'ERROR: %s' % e
        print(msg)
        print(traceback.format_exc())
        errors.append(msg)

    if errors:
        exit(1)


if __name__ == '__main__':
    main()
