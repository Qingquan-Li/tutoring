import NavBar from "../common/NavBar"
import Illustration from "./Illustration";

export default function Home() {
  return (
    <div className="container">
      {/* <div className="row"> */}
        <NavBar />
        <h1>Tutoring</h1>
        <Illustration />
      {/* </div> */}
    </div>
  );
}
