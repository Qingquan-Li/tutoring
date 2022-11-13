// import professor from '../assets/professor.svg';
import tutoring from '../assets/tutoring.svg';

// Use svg in img tag in React.js:
// Reference: https://stackoverflow.com/questions/52037007/svg-size-in-react
// Step#1: Remove `width="" height=""` from the original svg

export default function Illustration() {
  return (
    <div className='row justify-content-center mt-5'>
      {/* https://getbootstrap.com/docs/5.2/layout/breakpoints/ */}
      <div className="col-8 col-md-6 col-lg-4  mt-4">
        <img
          src={tutoring}
          // style={{ transform: "scale(0.5)" }}
          alt="illustration"
        />
      </div>
    </div>
  )
}
