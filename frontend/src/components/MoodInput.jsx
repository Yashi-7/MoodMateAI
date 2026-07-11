import {useState} from "react";
import ResultCard from "./ResultCard";


function MoodInput(){

    const [text,setText] = useState("");

    const [result,setResult] = useState(null);



    const analyzeMood = async()=>{


        const response = await fetch(
            "http://127.0.0.1:5000/predict",
            {
                method:"POST",

                headers:{
                    "Content-Type":"application/json"
                },

                body:JSON.stringify({
                    text:text
                })

            }
        );


        const data = await response.json();

        setResult(data);

    }



    return(

        <>

        <div className="mood-box">


            <textarea

            placeholder="Write how you feel today..."

            value={text}

            onChange={(e)=>setText(e.target.value)}

            />


            <button onClick={analyzeMood}>
                Analyze Mood ✨
            </button>


        </div>


        <ResultCard result={result}/>


        </>

    )

}


export default MoodInput;