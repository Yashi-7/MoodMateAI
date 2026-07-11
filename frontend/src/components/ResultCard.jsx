function ResultCard({result}){

    if(!result){
        return null;
    }


    return(

        <div className="result-card">

            <h1>
                {result.emoji} {result.emotion}
            </h1>


            <h3>
                Confidence: {result.confidence}%
            </h3>


            <p>
                {result.quote}
            </p>


            <h2>
                🎵 Recommended Songs
            </h2>


            <ul>

                {result.songs.map((song,index)=>(

                    <li key={index}>
                        {song}
                    </li>

                ))}

            </ul>


        </div>

    )

}

export default ResultCard;