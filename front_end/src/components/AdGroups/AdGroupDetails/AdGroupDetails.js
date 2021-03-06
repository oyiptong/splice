import React, { Component, PropTypes } from 'react';
import { Link } from 'react-router';

import { formatDate } from 'helpers/DateHelpers';

export default class AdGroupDetails extends Component {
  render() {
    const data = this.props.AdGroup.details;

    let categories = '';

    if(data !== undefined && data.categories !== undefined && data.categories !== null ){
      data.categories.map(function(val, index){
        if(index !== 0){
          categories += ', ';
        }
        categories += val;
      });
    }

    const suggestedFields = (
        <div>
          <p><strong>Explanation:</strong> {data.explanation}</p>
          <p><strong>Frequency Cap Daily:</strong> {data.frequency_cap_daily}</p>
          <p><strong>Frequency Cap Total:</strong> {data.frequency_cap_total}</p>
          <p><strong>Categories:</strong> {categories}</p>
        </div>
      );


    let details;
    if (this.props.AdGroup.details !== undefined) {
      details = (
        <div className="details-panel">
          <div className="details-panel-header">
            <div className={'details-panel-status ' + ((data.paused) ? 'paused' : 'active')}>{(data.paused) ? 'PAUSED' : 'ACTIVE'}</div>
            <div className="table-cell">
              <h2 className="details-panel-name">{data.name}</h2>
              <div className="details-panel-id">ID: {data.id}</div>
            </div>

            <div className="details-edit-link">
              <Link className="" to={'/adgroups/' + data.id + '/edit'} title="Edit">
                <i className="fa fa-pencil"></i>
              </Link>
            </div>
          </div>
          <div className="details-panel-body">
            <p><strong>Type:</strong> {_.capitalize(data.type)}</p>
            {(data.type === 'suggested') ? suggestedFields : null }
            <p><strong>Locale:</strong> {data.locale}</p>
            <p><strong>Created:</strong> {formatDate(data.created_at, 'M/D/YYYY')}</p>
          </div>
        </div>
      );
    } else {
      details = <img src={__CONFIG__.WEBPACK_PUBLIC_PATH + 'public/img/ajax-loader-navy.gif'}/>;
    }

    return details;
  }
}

AdGroupDetails.propTypes = {
  AdGroup: PropTypes.object.isRequired
};
