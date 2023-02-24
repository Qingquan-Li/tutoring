import Illustration from "./Illustration";
import MeetingList from "./MeetingList";
import "./index.css";

const AdsByGoogle = () => {
  (window.adsbygoogle = window.adsbygoogle || []).push({})
  return (
      <div>
          <ins class="adsbygoogle"
              style={{display:'block'}}
              data-ad-client="ca-pub-5622524728195625"
              data-ad-slot="7048770259"
              data-ad-format="auto"
              data-full-width-responsive="true">
          </ins>
      </div>
  )
}

export default function Home() {
  return (
    <div className="container home-container">
        <AdsByGoogle />
        <Illustration />
        <MeetingList />
    </div>
  );
}
