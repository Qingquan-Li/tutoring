import Illustration from "./Illustration";
import MeetingList from "./MeetingList";
import "./index.css";

export default function Home() {
  return (
    <div className="container home-container">
        <Illustration />
        <MeetingList />
    </div>
  );
}
