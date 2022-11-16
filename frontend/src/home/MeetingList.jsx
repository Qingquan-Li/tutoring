/**
 * TODO: pagination
 */

import axios from 'axios';
import { useEffect, useState } from 'react';
import './MeetingList.css'

const client = axios.create({
  baseURL: 'http://192.168.0.118:8000/api/v1/'
  // production:
  // baseURL: 'https://tutoring.helpyourmath/api/v1/'
});

export default function MeetingList() {
  const [meetings, setMeetings] = useState([]);

  useEffect(() => {
    client
      .get('meetings/')
      .then((response) => {
        setMeetings(response.data);
        // console.log(response);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <div className='row justify-content-center mt-5'>
      {/* <h4>Tutoring Session List</h4> */}
      {meetings.map((meeting) => {
        if (meeting.is_active) {
          return (
            <div className='card col-11 col-lg-8 mb-4' key={meeting.id}>
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
                  Meeting time: {meeting.meeting_time}
                </div>
                {/* <a href="#" className="btn btn-outline-primary mt-3">
                  View details
                </a> */}
                <button type="button" className="btn btn-outline-primary mt-3">
                  View details
                </button>
              </div>
            </div>
          );
        } else {
          return null;
        }
      })}
    </div>
  )
}
