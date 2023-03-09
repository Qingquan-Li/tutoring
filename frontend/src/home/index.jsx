import Illustration from "./Illustration";
import MeetingList from "./MeetingList";
import AdsByGoogle from "./AdsByGoogle";
import Announcement from "./Announcement";
import "./index.css";

export default function Home() {    
  return (
    <div className="container home-container">
        <AdsByGoogle />
        <Announcement />
        <Illustration />
        <MeetingList />
    </div>
  );
}
