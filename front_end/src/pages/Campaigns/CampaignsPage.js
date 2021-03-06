import React, { Component } from 'react';
import { connect } from 'react-redux';
import { pageVisit } from 'actions/App/AppActions';
import { fetchCampaigns } from 'actions/Campaigns/CampaignActions';

import CampaignList from 'components/Campaigns/CampaignList/CampaignList';

class CampaignsPage extends Component {
  componentDidMount() {
    const { dispatch } = this.props;

    pageVisit('Campaigns', this);

    if (this.props.location.query.accountId !== undefined) {
      dispatch(fetchCampaigns(this.props.location.query.accountId));
    }
  }

  render() {
    return (
      <div>
        <h1>Campaigns</h1>
        <CampaignList rows={this.props.Campaign.rows}
                      isFetching={this.props.Campaign.isFetching}/>
      </div>
    );
  }
}

CampaignsPage.propTypes = {};

// Which props do we want to inject, given the global state?
function select(state) {
  return {
    Account: state.Account,
    Campaign: state.Campaign
  };
}

// Wrap the component to inject dispatch and state into it
export default connect(select)(CampaignsPage);
