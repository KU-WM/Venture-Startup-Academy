import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../css/Login.css"

function Login () {
    const [modalOpen, setModalOpen] = useState(false);
    const navigate = useNavigate();

    const datahandler = () => {
        var BirthDay = document.getElementById('Day').value;

        if(BirthDay.length !== 10 || BirthDay[4] !== "-" || BirthDay[7] !== "-") {
            setModalOpen(true);
        }
        else {
            window.localStorage.setItem("BirthDay", BirthDay);
            window.localStorage.setItem("Logined", true);
            navigate('/')
        }
    }

    const Modal = (props) => {
        const { open, close, header } = props;
      
        return (
            <div className={open ? 'openedModalBack' : "modelBack"}>     
                <div className={open ? 'openedModal' : 'modal'}>
                {open ? (
                    <section>
                        <div>
                        {header}
                        </div>
                        <main className="onModal">
                            "날짜 입력이 잘못되었습니다."
                        </main>
                        <footer>
                        <button className="close" onClick={close}>
                            close
                        </button>
                        </footer>
                    </section>
                ) : null}
                </div>
            </div>
        )
    }

    const closeModal = () => {
        setModalOpen(false)
        window.location.reload();
    }

    const keyPress = (e) => {
        if(e.key === "Enter") {
            datahandler()
        }
    }

    const login = () => {
        navigate("/login")
    }

    const home = () => {
        navigate("/")
    }

    return (
        <React.Fragment>
            <header>
                <div className="teamName">
                    D & P COMMERCE
                </div>
                <button onClick={home} className="Home">
                    Home
                </button>
                <button onClick={login} className="loginBtn">
                    Login
                </button>
            </header>
            <section className="loginSection">
                <div className="login">
                    Login
                </div>
                <div className="line"></div>
                <div className="Id">
                    <div className="birth">
                        Your Brith
                    </div>
                    <input
                        id="Day"
                        className="birth"
                        placeholder="YYYY-MM-DD"
                        onKeyDown={keyPress}
                    />
                    <div className="warn">
                        *정확한 생년월일을 입력해 주세요
                    </div>
                </div>
                <div className="line"></div>
                <button className="loginBtn" onClick={datahandler}>Login</button>
                <Modal open={modalOpen} close={closeModal} header="날짜 입력 오류!"></Modal>
            </section>
        </React.Fragment>
    )
}

export default Login;