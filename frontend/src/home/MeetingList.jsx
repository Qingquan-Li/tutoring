/**
 * TODO: pagination
 */

import axios from 'axios';
import { useEffect, useMemo, useState } from 'react';
import { Link } from 'react-router-dom';
import './MeetingList.css'
import { RootAPIURL } from '../common/RootAPIURL';

const client = axios.create({
  baseURL: RootAPIURL,
});

export default function MeetingList() {
  const [meetings, setMeetings] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    client
      .get('meetings/')
      .then((response) => {
        setMeetings(response.data);
      })
      .catch((error) => {
        console.log(error);
        setError(error);
      });
  }, []);

  const meetingList = useMemo(()=>{
    const now = new Date();
    const list = meetings.sort((a,b)=>new Date(a.meeting_time)-new Date(b.meeting_time))
    .map((meeting) => {
      let date = new Date(meeting.meeting_time);
      if (meeting.is_active && date > now) {
        return (
          <div
            className='card col-11 col-lg-8 mb-4 meeting-list-card'
            key={meeting.id}
          >
            <div className='card-body'>
              <h5 className='card-title'>
                {meeting.subject}
              </h5>
              <div className='py-2'>
                <img
                  loading='lazy'
                  className='avatar'
                  src={meeting.publisher.avatar_url}
                  alt={meeting.publisher.name}
                />
                <p className='d-inline px-2 tutor-name'>
                  Tutor: {meeting.publisher.name}
                </p>
              </div>
              <p className='card-text pt-2'>
                {meeting.summary}
              </p>
              <div className='way-of-meeting'>
                Meet: {meeting.way_of_meeting}
              </div>
              <div className='meeting-time'>
                Meeting time: {date.toLocaleString().slice(0,-6)+date.toLocaleString().slice(-2)}
              </div>
              {/* <a href="#" className="btn btn-outline-primary mt-3">
                View details
              </a> */}
              <Link to={`meetings/${meeting.id}`}>
                <button type="button" className="btn btn-outline-primary mt-3">
                  View details
                </button>
              </Link>
            </div>
          </div>
        );
      } else {
        return null;
      }
    })
    return list;
  },[meetings])

  if (error) {
    return (
      `An error has occurred: ${error.message}`
    );
  }

  return (
    <div className='row justify-content-center mt-5'>
      {/* <h4>Tutoring Session List</h4> */}
      {meetingList}
    </div>
  )
}
