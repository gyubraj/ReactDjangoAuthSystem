import { connect } from 'react-redux';
import { verify } from '../actions/auth';
import { Redirect } from 'react-router-dom';
import { useState } from 'react';


const Activate = ({ match, verify }) => {
    const [verified, setVerified] = useState(false);
    const verify_account = (e) => {
        const uid = match.params.uid;
        const token = match.params.token;
        verify(uid, token);
        setVerified(true);
    };

    if (verified) {
        return <Redirect to='/' />
    }
    return (
        <div className='container'>
            <div className='d-flex flex-column justify-content-center align-items-center' style={{ marginTop: '200px' }}>
                <h1>Verify your Account</h1>
                <button
                    onClick={verify_account}
                    style={{ marginTop: '50px' }}
                    type='button'
                    className='btn btn-primary'>
                    VERIFY
                </button>

            </div>
        </div>
    )
}
export default connect(null, { verify })(Activate);