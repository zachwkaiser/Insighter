import { Link } from 'react-router-dom'
import './style.css'

export function Login() {
  return (
      <div className="page-container">
        <div className="login-container">
          <h1 className="welcome-heading">Hello, welcome to Insighter!</h1>
          <p className="welcome-subheading">Please enter your details to continue.</p>
          <form>
            <div className="form-group">
              <label htmlFor="email">Email</label>
              <input type="email" id="email" name="email" />
            </div>
            <div className="form-group">
              <label htmlFor="password">Password</label>
              <input type="password" id="password" name="password" />
            </div>
            <button type="submit" className="btn-primary">Login</button>
          </form>
          <p className="signup-link">Don't have an account? <Link to="/signup">Sign up</Link></p>
        </div>
      </div>
  )  
}
