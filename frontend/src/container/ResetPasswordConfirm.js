import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password_confirm } from '../actions/auth'

const ResetPasswordConfirm = ({ match, reset_password_confirm }) => {

    const [requestSent, setRequestSent] = useState(false);

    const [formData, setFormData] = useState({
        new_password: '',
        re_new_password: ''
    });

    const { new_password, re_new_password } = formData;
    const onChange = event => setFormData({
        ...formData,
        [event.target.name]: event.target.value
    });

    const onSubmit = e => {
        e.preventDefault();
        const uid = match.params.uid;
        const token = match.params.token;


        reset_password_confirm(uid, token, new_password, re_new_password);
        setRequestSent(true);

    };

    //If user is auhenticated then redirect them to the homepage
    if (requestSent) {
        return <Redirect to='/' />
    }

    return (
        <div className='container mt-5'>
            <h1>RESET YOUR PASSWORD</h1>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='New Password'
                        name='new_password'
                        value={new_password}
                        onChange={e => onChange(e)}
                        minLength='8'
                        required
                    />
                </div>
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='Confirm Password'
                        name='re_new_password'
                        value={re_new_password}
                        onChange={e => onChange(e)}
                        minLength='8'
                        required
                    />
                </div>
                <button className='btn btn-primary mt-3' type='submit'>Reset</button>
            </form>

        </div>
    );
};


export default connect(null, { reset_password_confirm })(ResetPasswordConfirm);