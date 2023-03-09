import { useEffect } from "react";

const AdsByGoogle = () => {

    useEffect(()=>{
        const script = document.createElement('script');
        script.async = true;
        script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2226955251055997'
        document.head.appendChild(script);
    
        (window.adsbygoogle = window.adsbygoogle || []).push({});
    }, []);

    return(
        <div>
            <script
            data-ad-client = "ca-pub-2226955251055997"
            async
            src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2226955251055997"
            />
            <ins 
                className="adsbygoogle"
                style={{display:'block'}}
                data-ad-client="ca-pub-2226955251055997"
                data-ad-slot="7048770259"
                data-ad-format="auto"
                data-full-width-responsive="true">
            </ins>
        </div>
    )
}

export default AdsByGoogle;