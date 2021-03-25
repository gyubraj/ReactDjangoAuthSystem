import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Home from './container/Home';
import Activate from './container/Activate';
import ResetPassword from './container/ResetPassword';
import ResetPasswordConfirm from './container/ResetPasswordConfirm';
import Login from './container/Login';
import Signup from './container/Signup';
import Layout from './hoc/Layout';
import { Provider } from 'react-redux';
import store from './store/store';

const App = () => (
    <Provider store={store}>
        <BrowserRouter>
            <Layout>
                <Switch>
                    <Route exact path='/' component={Home} />
                    <Route exact path='/login' component={Login} />
                    <Route exact path='/signup' component={Signup} />
                    <Route exact path='/reset-password' component={ResetPassword} />
                    <Route exact path='/password/reset/confirm/:uid/:token' component={ResetPasswordConfirm} />
                    <Route exact path='/activate/:uid/:token' component={Activate} />

                </Switch>
            </Layout>
        </BrowserRouter>
    </Provider>

);

export default App;