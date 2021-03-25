import React, { useState } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { signup } from '../actions/auth'
import axios from 'axios';

const Signup = ({ signup, isAuthenticated }) => {

    const [accountCreated, setAccountCreated] = useState(false);

    const [formData, setFormData] = useState({
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        re_password: ''
    });

    const { first_name, last_name, email, password, re_password } = formData;
    const onChange = event => setFormData({
        ...formData,
        [event.target.name]: event.target.value
    });

    const onSubmit = e => {
        e.preventDefault();

        if (password === re_password) {
            signup(first_name, last_name, email, password, re_password);
            setAccountCreated(true);
        }

    };

    // const continueWithGoogle = async () => {

    //     try {
    //         const res = await axios.get(`${process.env.REACT_APP_API_URL}/auth/o/google-oauth2/?redirect_uri=http://localhost:8000`);
    //         window.location.replace(res.data.authorization_url);

    //     } catch (err) {

    //     }

    // }


    //If user is auhenticated then redirect them to the homepage
    if (isAuthenticated) {
        return <Redirect to='/' />
    }

    if (accountCreated) {
        return <Redirect to='/login' />
    }

    return (
        <div className='container mt-5'>
            <h1>Sign Up</h1>
            <p>SignUp to date app</p>
            <form onSubmit={e => onSubmit(e)}>
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='text'
                        placeholder='First Name'
                        name='first_name'
                        value={first_name}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='text'
                        placeholder='Last Name'
                        name='last_name'
                        value={last_name}
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
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
                <div className='form-group mt-3'>
                    <input
                        className='form-control'
                        type='password'
                        placeholder='Confirm Password'
                        name='re_password'
                        value={re_password}
                        minLength='8'
                        onChange={e => onChange(e)}
                        required
                    />
                </div>
                <button className='btn btn-primary mt-3' type='submit'>Login</button>
            </form>
            {/* <button className='btn btn-danger mt-3' onClick={continueWithGoogle}>
                CONTINUE WITH GOOGLE
            </button> */}
            {/* <p className='mt-3'>OR</p>
            <button className='btn btn-primary '>
                CONTINUE WITH FACEBOOK
            </button> */}

        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
});

export default connect(mapStateToProps, { signup })(Signup);