import React, { useState } from 'react';
import { connect } from 'react-redux';
import * as actions from '../redux/actions';
import { Layout, Drawer } from 'antd';

import Routes from './Routes';
import NavBar from '../components/NavBar';
import Footer from '../components/Footer';
import SidebarMenu from '../containers/SidebarMenu';
import MentorHeader from '../containers/MentorHeader';

const MainLayout = ( {user} ) => {
    // sidebar collapsed state
    const [drawerVisible, setDrawerVisible] = useState(false);

    const onDrawerClose = () => setDrawerVisible(prev => !prev);

    const { Content } = Layout;

  return (
    <div>
      <div>
        <Layout>
          <NavBar />
          <Content
            className="site-layout"
            style={{ padding: '50px', marginTop: 64, backgroundColor: '#fffff6' }}
          >
            {user.id ?
            <div>
              <Drawer
                title="VBB Portal"
                placement="left"
                closable={true}
                onClose={onDrawerClose}
                visible={drawerVisible}
                width={250}
                bodyStyle={{ paddingRight: '0px', paddingLeft: '0px' }}
              >
                <SidebarMenu />
              </Drawer>
              <MentorHeader onDrawerClose={onDrawerClose} />
            </div>
            :
            ""
            }
            <div style={{ padding: 24, minHeight: 380 }}>
              <Routes />
            </div>
          </Content>
          <Footer />
        </Layout>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
  user: state.user
  };
};

export default connect(mapStateToProps, actions)(MainLayout);
