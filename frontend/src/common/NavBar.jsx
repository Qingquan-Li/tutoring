import React from 'react';

export default function NavBar() {
  return (
    <>
      <nav className="navbar navbar-expand-lg fixed-top navbar-light bg-light">
        <div className="container-md">
          <a className="navbar-brand mb-0 h1" href="/">Tutoring</a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavAltMarkup"
            aria-controls="navbarNavAltMarkup"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav ms-auto">
              <a className="nav-link" href="/contact/">Contact Us</a>
              <a className="nav-link" href="/admin/">Admin</a>
            </div>
          </div>
        </div>
      </nav>
    </>
  );
}