import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password } from '../actions/auth'

const ResetPassword = ({ reset_password }) => {

    const [requestSent, setRequestSent] = useState(false);

    const [formData, setFormData] = useState({
        email: ''
    });

    const { email } = formData;
    const onChange = event => setFormData({
        ...formData,
        [event.target.name]: event.target.value
    });

    const onSubmit = e => {
        e.preventDefault();

        reset_password(email);
        setRequestSent(true);

    };

    //If user is auhenticated then redirect them to the homepage
    if (requestSent) {
        return <Redirect to='/' />
    }

    return (
        <div className='container mt-5'>
            <h1>RESET PASSWORD</h1>
            <p>Enter Your Email</p>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='email'
                        placeholder='Email'
                        name='email'
                        value={email}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <button className='btn btn-primary mt-3' type='submit'>Reset</button>
            </form>

        </div>
    );
};


export default connect(null, { reset_password })(ResetPassword);