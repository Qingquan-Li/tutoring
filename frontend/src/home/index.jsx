import NavBar from "../common/NavBar"
import Illustration from "./Illustration";
import MeetingList from "./MeetingList";
import "./index.css";

export default function Home() {
  return (
    <div className="container">
        <NavBar />
        <Illustration />
        <MeetingList />
    </div>
  );
}
