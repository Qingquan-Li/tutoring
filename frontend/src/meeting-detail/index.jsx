import { useParams } from "react-router-dom";
import axios from "axios";
import { useEffect, useMemo, useState } from "react";
import RegistrationForm from "./RegistrationForm";
import "bootstrap-icons/font/bootstrap-icons.css";
import "./index.css";
import { RootAPIURL } from "../common/RootAPIURL";

const baseURL = RootAPIURL;

export default function MeetingDetail() {
  const params = useParams();
  const [meeting, setMeeting] = useState({});
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get(baseURL + `meetings/${params.meetingId}/`)
      .then((response) => {
        setMeeting(response.data);
      })
      .catch((error) => {
        console.log(error);
        setError(error);
      });
  }, [params.meetingId]);

  const isDisabled = useMemo(()=>{
    const now = new Date();
    let result = new Date(meeting.meeting_time) < now;
    return result;
  },[meeting])

  if (error) {
    return (
      `An error has occurred: ${error.message}`
    );
  }

  return (
    <div className="container meeting-detail-container">
      <div className='row justify-content-center'>
        <div className="col-lg-8">
          <h1>{meeting.subject}</h1>
          <div className='py-2'>
            <img
              loading='lazy'
              className='avatar'
              src={meeting.publisher?.avatar_url}
              alt={meeting.publisher?.name}
            />
            <p className='d-inline px-2'>
              Tutor: {meeting.publisher?.name}
            </p>
          </div>
          <p className='summary pt-2'>
            {meeting.summary}
          </p>
          {!meeting.additional_notes ? (
              null
            ) : (
              <p>
              <i className="bi bi-info-circle"></i>{' '}
              Additional notes: {meeting.additional_notes}
              </p>
          )}
          <p>
            {meeting.way_of_meeting === 'in-person' ? (
              <i className="bi bi-person-video3"></i>
            ) : (
              <i className="bi bi-camera-video"></i>
            )}
            <span>&nbsp;</span>
            Meet: {meeting.way_of_meeting}
            <br />
            <i className="bi bi-clock"></i>{' '}
            Meeting time: {
              // If meeting.meeting_time is not null, then format it
              // using the Intl.DateTimeFormat object.
              meeting.meeting_time
              ? new Intl.DateTimeFormat("en-US", {
                  year: "numeric",
                  month: "numeric",
                  day: "numeric",
                  hour: "2-digit",
                  minute: "2-digit",
                  hour12: true,
                }).format(new Date(meeting.meeting_time))
              : null
            }
          </p>
          <br />
          <RegistrationForm isDisabled={isDisabled}/>
        </div>
      </div>
    </div>
    
  )
}
