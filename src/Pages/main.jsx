import React from "react";
import { useNavigate } from "react-router-dom";
import Neet from '../Img/니트.png'
import Headset from '../Img/헤드폰.png'
import Shoose from '../Img/운동화.png'
import Blue from '../Img/블루베리.png'
import '../css/Main.css'

function Main () {
    const navigate = useNavigate();

    const login = () => {
        navigate("/login")
    }

    const home = () => {
        navigate("/")
    }

    const isLogined = () => {
        const login = window.localStorage.getItem("Logined") ? true : false;
        if (login) {
            navigate('/buy')
        }
        else {
            navigate("/login")
        }
    }

    const delayPage = () => {
        navigate("/delay")
    }

    return (
        <React.Fragment>
            <header>
                <div className="teamName" onClick={delayPage}>
                    D & P COMMERCE
                </div>
                <button onClick={home} className="Home">
                    Home
                </button>
                <button onClick={login} className="loginBtn">
                    Login
                </button>
            </header>
            <section className="content">
                <div className="nameTop">
                    BLACK FRIDAY
                </div>
                <div className="nameBottom">
                    PROMOTION
                </div>
                <div>
                    <img onClick={isLogined} src={Shoose} alt="런닝화"></img>
                    <img onClick={isLogined} src={Headset} alt="헤드셋"></img>
                    <img onClick={isLogined} src={Neet} alt="런닝화"></img>
                    <img onClick={isLogined} src={Blue} alt="블루베리"></img>
                </div>
            </section>
        </React.Fragment>
    )
}

export default Main;