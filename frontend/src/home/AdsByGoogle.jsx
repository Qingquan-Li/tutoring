import { useEffect } from "react";

const AdsByGoogle = () => {

    useEffect(()=>{
        const script = document.createElement('script');
        script.async = true;
        // Test src
        script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5622524728195625';
        // Production scr
        // script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-2226955251055997'
        document.head.appendChild(script);
    
        (window.adsbygoogle = window.adsbygoogle || []).push({});
    }, []);

    return(
        <div>
            <script
            data-ad-client = "ca-pub-5622524728195625"
            async
            src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-5622524728195625"
            />
            <ins 
                className="adsbygoogle"
                style={{display:'block'}}
                data-ad-client="ca-pub-5622524728195625"
                data-ad-slot="7048770259"
                data-ad-format="auto"
                data-full-width-responsive="true">
            </ins>
        </div>
    )
}

export default AdsByGoogle;