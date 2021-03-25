import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { login } from '../actions/auth'
import axios from 'axios';

const Login = ({ login, isAuthenticated }) => {

    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const { email, password } = formData;
    const onChange = event => setFormData({
        ...formData,
        [event.target.name]: event.target.value
    });

    const continueWithGoogle = async () => {

        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/o/google-oauth2/?redirect_uri=http://localhost:8000`);
            window.location.replace(res.data.authorization_url);

        } catch (err) {

        }

    }

    const onSubmit = e => {
        e.preventDefault();

        login(email, password)

    };

    //If user is auhenticated then redirect them to the homepage
    if (isAuthenticated) {
        return <Redirect to='/' />
    }

    return (
        <div className='container mt-5'>
            <h1>Sign In</h1>
            <p>Sign into your account</p>
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
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='Password'
                        name='password'
                        value={password}
                        minLength='8'
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <button className='btn btn-primary mt-3' type='submit'>Login</button>
            </form>

            <button className='btn btn-danger mt-3' onClick={continueWithGoogle}>
                CONTINUE WITH GOOGLE
            </button>
            <p className='mt-3'>OR</p>
            <button className='btn btn-primary '>
                CONTINUE WITH FACEBOOK
            </button>

            <p className='mt-3'>
                Don't have an Account ? <Link to='/signup'>Sign Up</Link>
            </p>
            <p className='mt-3'>
                Forgot your password ? <Link to='/reset-password'>Reset Password</Link>
            </p>

        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { login })(Login);