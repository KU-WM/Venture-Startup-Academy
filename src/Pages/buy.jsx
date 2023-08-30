import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import '../css/Buy.css'
import star from '../Img/별.png'
import Black from '../Img/블랙프라이데이별.png'

function Buy ()  {
    const Birth = window.localStorage.getItem("BirthDay")
    const [modalOpen, setModalOpen] = useState(false);
    const [dateOpen, setDateOpen] = useState(false);

    const navigate = useNavigate()

    const closeModal = () => {
        setModalOpen(false)
    }

    const closeDate = () => {
        setDateOpen(false)
    }

    const canGet = () => {
        if (Birth.slice(5, 7) === '07' || Birth.slice(5, 7) === '08') {
            setDateOpen(true)
        }
        else {
            setModalOpen(true)
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
                            "신청 가능한 날짜가 아닙니다."
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

    const Date = (props) => {
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
                            "신청되었습니다! 발표일을 기대해 주세요!"
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
            <section className="buySection">
                <div className="buying">
                    RESERVATION
                </div>
                <div className="line"></div>
                <div>
                    <ul>
                        <li>SAT</li>
                        <li>SUN</li>
                        <li>MON</li>
                        <li>TUE</li>
                        <li>WED</li>
                        <li>THU</li>
                        <li>FRI</li>
                    </ul>
                </div>
                <div className="line"></div>
                <ul>
                    <li>18</li>
                    <li>19</li>
                    <li>20</li>
                    <li>21</li>
                    <li>22</li>
                    <li>23</li>
                    <li>24</li>
                </ul>
                <img className="star" src={star} alt="별" />
                <img className="black" src={Black} alt="블프" />
                <div className="line"></div>
                <button className="reserve" onClick={canGet}>RESERVE</button>
            </section>
            <footer>
                <div>
                    * 생년월일의 월별로 신청 가능한 날짜가 다르니 확인하시기 바랍니다.
                </div>
                <div>
                    * 오늘은 목요일로 7, 8월에 태어나신 분들만 신청이 가능합니다.
                </div>
                <div>
                    * 이번주 금요일에 블랙프라이데이 할인 상품들의 추첨이 개시됩니다.
                </div>
            </footer>
            <Modal open={modalOpen} close={closeModal} header="신청 날짜 오류!"></Modal>
            <Date open={dateOpen} close={closeDate} header="신청 성공!"></Date>
        </React.Fragment>
    )
}

export default Buy;