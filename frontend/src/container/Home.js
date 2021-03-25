import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
const Home = ({ mapStateToProps }) => (
    <div className='container'>
        <div class="jumbotron mt-5 ">
            <h1 class="display-4">Date App</h1>
            <p class="lead">You can have fun here.Lets make love.</p>
            <hr class="my-4" />
            <p>Please Click Below to Navigate.</p>
            {mapStateToProps ? <Link class="btn btn-primary btn-lg" to='/signup' role="button">Sign up</Link> : <Link class="btn btn-primary btn-lg" to='/login' role="button">Log In</Link>}
        </div>
    </div>

)

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated
})
export default connect(mapStateToProps)(Home);