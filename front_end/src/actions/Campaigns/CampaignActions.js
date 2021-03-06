import fetch from 'isomorphic-fetch';
import * as config from 'helpers/config';
import { fetchHelper } from 'helpers/FetchHelpers';

const apiUrl = config.get('API_URL');

export const REQUEST_CREATE_CAMPAIGN = 'REQUEST_CREATE_CAMPAIGN';
export const RECEIVE_CREATE_CAMPAIGN = 'RECEIVE_CREATE_CAMPAIGN';

export const REQUEST_UPDATE_CAMPAIGN = 'REQUEST_UPDATE_CAMPAIGN';
export const RECEIVE_UPDATE_CAMPAIGN = 'RECEIVE_UPDATE_CAMPAIGN';

export const REQUEST_BULK_UPLOAD = 'REQUEST_BULK_UPLOAD';
export const RECEIVE_BULK_UPLOAD = 'RECEIVE_BULK_UPLOAD';

export const REQUEST_CAMPAIGNS = 'REQUEST_CAMPAIGNS';
export const RECEIVE_CAMPAIGNS = 'RECEIVE_CAMPAIGNS';

export const REQUEST_CAMPAIGN = 'REQUEST_CAMPAIGN';
export const RECEIVE_CAMPAIGN = 'RECEIVE_CAMPAIGN';

export const CAMPAIGN_SET_FILTER = 'CAMPAIGN_SET_FILTER';

export const CAMPAIGN_SET_DETAILS_VAR = 'CAMPAIGN_SET_DETAILS_VAR';

export function campaignSetDetailsVar(variable, value){
  return {type: CAMPAIGN_SET_DETAILS_VAR, variable: variable, value: value};
}

export function requestCreateCampaign() {
  return {type: REQUEST_CREATE_CAMPAIGN};
}

export function receiveCreateCampaign(json) {
  return {
    type: RECEIVE_CREATE_CAMPAIGN,
    json: json
  };
}

export function requestUpdateCampaign() {
  return {type: REQUEST_UPDATE_CAMPAIGN};
}

export function receiveUpdateCampaign(json) {
  return {
    type: RECEIVE_UPDATE_CAMPAIGN,
    json: json
  };
}

export function requestBulkUpload() {
  return {type: REQUEST_BULK_UPLOAD};
}

export function receiveBulkUpload(json) {
  return {
    type: RECEIVE_BULK_UPLOAD,
    json: json
  };
}

export function requestCampaign() {
  return {type: REQUEST_CAMPAIGN};
}
export function receiveCampaign(json) {
  return {
    type: RECEIVE_CAMPAIGN,
    json: json
  };
}

export function requestCampaigns() {
  return {type: REQUEST_CAMPAIGNS};
}
export function receiveCampaigns(json) {
  return {
    type: RECEIVE_CAMPAIGNS,
    json: json
  };
}

export function campaignSetFilter(variable, value) {
  return {
    type: CAMPAIGN_SET_FILTER,
    variable: variable,
    value: value
  };
}

export function createCampaign(data) {
  // thunk middleware knows how to handle functions
  return function next(dispatch) {
    dispatch(requestCreateCampaign());
    // Return a promise to wait for
    const url = apiUrl + '/api/campaigns';
    const options = {
      method: 'post',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: data
    };
    return fetchHelper(url, options, receiveCreateCampaign, dispatch);
  };
}

export function updateCampaign(campaignId, data) {
  // thunk middleware knows how to handle functions
  return function next(dispatch) {
    dispatch(requestUpdateCampaign());
    // Return a promise to wait for
    const url = apiUrl + '/api/campaigns/' + campaignId;
    const options = {
      method: 'put',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: data
    };
    return fetchHelper(url, options, receiveUpdateCampaign, dispatch);
  };
}

export function bulkupload(campaignId, data){
  // thunk middleware knows how to handle functions
  return function next(dispatch) {
    dispatch(requestBulkUpload());
    // Return a promise to wait for
    const url = apiUrl + '/api/campaigns/' + campaignId + '/bulkupload';
    const options = {
      method: 'post',
      headers: {
        'Accept': 'application/json'
      },
      body: data
    };
    return fetchHelper(url, options, receiveBulkUpload, dispatch);
  };
}

export function fetchCampaign(campaignId) {
  // thunk middleware knows how to handle functions
  return function next(dispatch) {
    dispatch(requestCampaign());
    // Return a promise to wait for
    const url = apiUrl + '/api/campaigns/' + campaignId;
    return fetchHelper(url, null, receiveCampaign, dispatch);
  };
}

export function fetchCampaigns(accountId, past = null, scheduled = null, inFlight = null) {
  // thunk middleware knows how to handle functions
  return function next(dispatch, state) {
    dispatch(requestCampaigns());

    const campaign = state().Campaign;

    let p = past;
    if(p === null){
      p = campaign.filters.past;
    }
    let s = scheduled;
    if(s === null){
      s = campaign.filters.scheduled;
    }
    let i = inFlight;
    if(i === null){
      i = campaign.filters.inFlight;
    }

    const url = apiUrl + '/api/campaigns' +
      '?account_id=' + accountId +
      '&past=' + p +
      '&scheduled=' + s +
      '&in_flight=' + i;
    return fetchHelper(url, null, receiveCampaigns, dispatch);
  };
}
