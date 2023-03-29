import axios from "axios";
import { useParams } from "react-router-dom";
import { useMemo, useState } from "react";
import { RootAPIURL } from "../common/RootAPIURL";

const RegistrationAPIURL = RootAPIURL + 'registrations/';

// https://stackoverflow.com/questions/39254562/csrf-with-django-reactredux-using-axios
// https://www.techiediaries.com/django-react-forms-csrf-axios/
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axios.defaults.xsrfCookieName = "csrftoken";

export default function RegistrationForm({ isDisabled = false }) {
  const params = useParams();
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [emailAddress, setEmailAddress] = useState('');
  const [CUNYfirstID, setCUNYfirstID] = useState('');
  const [registrationSuccessFlag, setRegistrationSuccessFlag] = useState(false);
  const [error, setError] = useState(null);
  const [isShowValidated, setIsShowValidated] = useState(false);
  const isIdInvalid = useMemo(()=>{
    const checkId = [...CUNYfirstID].map(item => (item.charCodeAt() > 57 || item.charCodeAt() < 48)).some(item=>item);
    const result = (checkId || CUNYfirstID.length !== 8);
    return result
  },[CUNYfirstID])
  
  const isEmailInvalid = useMemo(()=>{
    if(emailAddress === ''){
      return true;
    }
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const result = !emailRegex.test(emailAddress);
    return result
  },[emailAddress])

  const handleSubmit = (e) => {
    e.preventDefault();
    setIsShowValidated(true);
    axios.post(RegistrationAPIURL, {
      meeting: params.meetingId,
      first_name: firstName,
      last_name: lastName,
      email: emailAddress,
      cunyfirst_id: CUNYfirstID,
    })
    .then((response) => {
      setRegistrationSuccessFlag(true);
      setFirstName('');
      setLastName('');
      setEmailAddress('');
      setCUNYfirstID('');
      setError(null);
    })
    .catch((error) => {
      console.log(error);
      setError(`An error has occurred: ${error.message}`);
    });
  }
  return (
    isDisabled?
    <div>
      Meeting Expired
    </div>:
    <div className="card border-secondary">
      <div className="card-header">
        Register Now
      </div>
      <div className="card-body">
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label className="form-label">First name*</label>
            <input
              type="text"
              className="form-control"
              value={firstName}
              // The target event property returns the element
              // that triggered the event.
              onChange={(e) => setFirstName(e.target.value)}
            />
            {isShowValidated && firstName === '' ? <div className="invalid">First name can not be empty.</div>:''}
          </div>
          <div className="mb-3">
            <label className="form-label">Last name*</label>
            <input
              type="text"
              className="form-control"
              value={lastName}
              onChange={(e) => setLastName(e.target.value)}
            />
            {isShowValidated && lastName === '' ? <div className="invalid">Last name can not be empty.</div>:''}
          </div>
          <div className="mb-3">
            <label className="form-label">Email address*</label>
            <input
              type="email"
              className="form-control"
              value={emailAddress}
              onChange={(e) => setEmailAddress(e.target.value)}
            />
            {isShowValidated && isEmailInvalid ? <div className="invalid">Email address is invalid.</div>:''}
          </div>
          <div className="mb-3">
            <label className="form-label">CUNYfirst ID*</label>
            <input
              type="text"
              className="form-control"
              value={CUNYfirstID}
              onChange={(e) => setCUNYfirstID(e.target.value)}
            />
            {isShowValidated && isIdInvalid ?<div className="invalid">CUNYfirst ID should be 8 digit numbers.</div>:''}
          </div>
          <button type="submit" className="btn btn-primary mt-3">
            Submit Registration
          </button>
          {registrationSuccessFlag ? (
            <div className="alert alert-success mt-5">
              <h4 className="alert-heading">Registration Success!</h4>
              <p>
                Thanks for your registration.
                The tutor will email you before the tutoring.
              </p>
            </div>
          ) : null}
          {error ? (
            <div className="alert alert-danger mt-5">
              {error}
            </div>
          ) : null}
        </form>
      </div>
    </div>

  );
}
