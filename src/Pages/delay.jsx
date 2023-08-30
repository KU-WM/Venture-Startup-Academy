import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import '../css/delay.css'
import delay from "../Img/delay.png"

function Delay () {
    const [wait, setWait] = useState(200)
    const navigate = useNavigate()

    useEffect(() => {
        wait > 0 && setTimeout(() => setWait(wait < 0 ? 0: wait - random(8, 30)), 1500);
        if (wait <= 0) {
            // navigate("/login")
        } 
    }, [wait])

    const random = (min, max) => {
        return Math.floor(Math.random() * (max - min) + min)
    }

    return (
        <React.Fragment>
            <div className="delay">
                <img className="delayImg" src={delay} alt="delay"></img>
                {/* <div className="service">서비스 접속 대기 중입니다.</div>
                <div>나의 순서</div>
                <div className="waiting">{wait > 0 ? wait : 0}</div>
                <div className="count">예상 대기 시간 : <span>{wait / 5 > 0 ? parseInt(wait / 5) : 0}초</span></div>
                <div>현재 사용자가 많아 접속이 지연되고 있습니다.</div>
                <div>잠시만 기다려주세요.</div>
                <div className="warning">재접속하시면 대기시간이 길어질 수 있습니다.</div> */}
            </div>
        </React.Fragment>
    )
}

export default Delay;