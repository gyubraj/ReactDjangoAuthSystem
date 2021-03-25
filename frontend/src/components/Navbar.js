import { Link } from 'react-router-dom';
import { logout } from '../actions/auth';
import { connect } from 'react-redux';
import { Fragment } from 'react';

const Navbar = ({ logout, isAuthenticated }) => {

    const guestView = (
        <Fragment>
            <li class="nav-item active">
                <Link class="nav-link" to='/login'>Log In</Link>
            </li>
            <li class="nav-item">
                <Link class="nav-link" to='/signup'>Sign Up</Link>
            </li>
        </Fragment>
    )
    const authView = (
        <li class="nav-item active">
            <a class="nav-link" href='/#' onClick={logout}>Log Out</a>
        </li>
    )



    return (
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <Link class="navbar-brand" to='/'>Date App</Link>
            <button
                class="navbar-toggler"
                type="button"
                data-toggle="collapse"
                data-target="#navbarNav"
                aria-controls="navbarNav"
                aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav">
                    <li class="nav-item">
                        <Link class="nav-link" to='/'>Home</Link>
                    </li>
                    {isAuthenticated ? authView : guestView}

                </ul>
            </div>
        </nav>
    )
}

const mapStateToProps = () => state => ({
    isAuthenticated: state.auth.isAuthenticated
})
export default connect(mapStateToProps, { logout })(Navbar);