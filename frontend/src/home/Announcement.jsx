import axios from 'axios';
import { useEffect, useState } from 'react';
import './Announcement.css'
import warningIcon from '../assets/warning-orange.png';
import { RootAPIURL } from '../common/RootAPIURL';

const client = axios.create({
  baseURL: RootAPIURL,
});

export default function Announcement() {
    const [message, setMessage] = useState('');
    const [error, setError] = useState(null);

    useEffect(() => {
        client
          .get('announcements/')
          .then((res) => {
            setMessage(res.data.pop().content)
          })
          .catch((error) => {
            console.log(error);
            setError(error);
          });
    }, [])

    if (error) {
        return (
          `An error has occurred: ${error.message}`
        );
    }

    return(
        <div className='emergency-banner-wrapper'>
            <figure className='alert' role = 'alert'>
                <img src={warningIcon} alt="warning"/>
                <figcaption>
                    {message}
                </figcaption>
            </figure>
        </div>
    )
}