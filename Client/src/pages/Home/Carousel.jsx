import { useEffect, useRef, useState } from 'react'
import styles from './Home.module.css'

let images = [
    {link : '/carousel/1.jpg', name : 1},
    {link : '/carousel/2.jpg', name : 2},
    {link : '/carousel/3.jpg', name : 3},
    {link : '/carousel/4.jpg', name : 4},
    {link : '/carousel/5.jpg', name : 5},
]

function Carousel(){
    let [imagePos , setImagePos] = useState(0)
    let leftBtnRef = useRef(null)

    function handleBtn(e){
        if (e.target.name == 'left')
            imagePos -= 1
        else
            imagePos += 1

        if (imagePos == -images.length)
            imagePos = 0

        if (imagePos == 1)
            imagePos = -(images.length -1)

        setImagePos(imagePos)
    }

    // useEffect(function(){
    //     setInterval(function(){
    //         leftBtnRef.current.click()
    //     } , 10000)
    // } , [])


    return (
        <div className={styles.carousel}>
            <button ref={leftBtnRef} className={styles.left} onClick={handleBtn} name='left' data-left>
                <img src="/left.svg" alt="left"/>
            </button>
            <button  className={styles.right} onClick={handleBtn} name='right' data-right>
                <img src="/right.svg" alt="right"/>
            </button>
            <ul>
                {images.map(function(i , ind){
                    return <img key={i.link} src={i.link} alt={i.name} style={{transform : `translateX(${imagePos*100}%)`}}/>
                })}
            </ul>
        </div>
    )
}

export default Carousel