import React from 'react';
import { PageHeader } from 'antd';
import { connect } from 'react-redux';
import * as actions from '../redux/actions';
import { MenuUnfoldOutlined } from '@ant-design/icons';

/**
 *  Top navigation bar for mentor
 * @param {Object} props.user Mentor profile information
 * @param {()=>void} props.onDrawerClose Function to toggle the left drawer for site nav
 * @returns React element
 */

const MentorHeader = ({ user, onDrawerClose }) => {

  return (
    <>
      <PageHeader
        theme="light"
        onBack={() => onDrawerClose()}
        backIcon={<MenuUnfoldOutlined />}
        title={`Hello, ${user.firstName} ${user.lastName || 'Mentor'}`}
        avatar={{
          src: 'https://picsum.photos/100',
        }}
      />
    </>
  );
}

const mapStateToProps = (state) => {
    return {
    logOut: state.logOut,
    user: state.user
    };
  };

  export default connect(mapStateToProps, actions)(MentorHeader);