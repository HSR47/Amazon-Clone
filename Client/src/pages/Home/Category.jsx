import { useEffect, useRef, useState } from 'react'
import styles from './Home.module.css'

function Category(){
    let [pos , setPos] = useState(0)
    let [btnVisibility , setBtnVisibility] = useState(false)
    let [hovering , setHovering] = useState(false)

    let ulRef = useRef(null)
    let totalElements = 12

    function handleBtnClick(e){
        let ulWidth = ulRef.current.offsetWidth
        let elementsVisible = Math.floor(ulWidth/250)
        let maxPos = totalElements*200 + (totalElements-1)*50 - (elementsVisible*200 + (elementsVisible-1)*50)

        let btn = e.target.closest('button')
        if (btn.name == 'left' && pos<0)
            pos += elementsVisible * 250
            if (pos>0)
                pos = 0
        
        else if (btn.name == 'right')
            pos -= elementsVisible * 250
            if (pos < (-maxPos))
                pos = -maxPos

        setPos(pos)
    }

    useEffect(function(){
        let ulWidth = ulRef.current.offsetWidth
        let elementsVisible = Math.floor(ulWidth/250)
        if (elementsVisible >= totalElements)
            setBtnVisibility(false)
        else
            setBtnVisibility(true)
    } , [])


    return (
        <div className={styles.category}>
            <h1 className={styles.title}>Shop by category</h1>
            <div className={styles.slider} onMouseEnter={function(){setHovering(true)}} onMouseLeave={function(){setHovering(false)}}>
                {btnVisibility==true && hovering==true &&
                    <>
                        <button className={styles.left} name='left' onClick={handleBtnClick}>
                            <img src="/left.svg" alt="left" />
                        </button>
                        <button className={styles.right} name='right' onClick={handleBtnClick}>
                            <img src="/right.svg" alt="right" />
                        </button>
                    </>
                }
                

                <ul ref={ulRef} style={{transform : `translateX(${pos}px)`}}>
                    <li>
                        <img src="/category/phone.jpg" alt="phone" />
                        <p>Phone</p>
                    </li>
                    <li>
                        <img src="/category/laptop.jpg" alt="laptop" />
                        <p>Laptop</p>
                    </li>
                    <li>
                        <img src="/category/tablet.jpg" alt="tablet" />
                        <p>Tablet</p>
                    </li>
                    <li>
                        <img src="/category/phone.jpg" alt="phone" />
                        <p>Phone</p>
                    </li>
                    <li>
                        <img src="/category/laptop.jpg" alt="laptop" />
                        <p>Laptop</p>
                    </li>
                    <li>
                        <img src="/category/tablet.jpg" alt="tablet" />
                        <p>Tablet</p>
                    </li>
                    <li>
                        <img src="/category/phone.jpg" alt="phone" />
                        <p>Phone</p>
                    </li>
                    <li>
                        <img src="/category/laptop.jpg" alt="laptop" />
                        <p>Laptop</p>
                    </li>
                    <li>
                        <img src="/category/tablet.jpg" alt="tablet" />
                        <p>Tablet</p>
                    </li>
                    <li>
                        <img src="/category/phone.jpg" alt="phone" />
                        <p>Phone</p>
                    </li>
                    <li>
                        <img src="/category/laptop.jpg" alt="laptop" />
                        <p>Laptop</p>
                    </li>
                    <li>
                        <img src="/category/tablet.jpg" alt="tablet" />
                        <p>Tablet</p>
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default Category