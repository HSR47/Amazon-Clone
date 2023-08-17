import { useEffect, useRef, useState } from 'react'
import styles from './Home.module.css'
import ProductSquare from './ProductSquare'


function ProductSlider({info}){
    let [pos , setPos] = useState(0)
    let ulRef = useRef(null)
    let prodSqWidth = 330
    let prodSqGap = 20

    let totalElements = info.products.length
    
    function handleBtnClick(e){
        let ulWidth = ulRef.current.offsetWidth
        let visibleElements = Math.floor(ulWidth/(prodSqWidth+prodSqGap))
        let maxPos = totalElements*prodSqWidth + (totalElements-1)*prodSqGap - (visibleElements*prodSqWidth + (visibleElements-1)*prodSqGap)

        let ele = e.target.closest('button')
        if (ele.name == 'left')
            pos += visibleElements * (prodSqWidth+prodSqGap)
        else
            pos -= visibleElements * (prodSqWidth+prodSqGap)

        if (pos>0)
            pos = 0
        if (pos < (-maxPos))
            pos = -maxPos
        
        setPos(pos)
    }

    return (
        <div className={styles.productSlider}>
            <h1 className={styles.heading}>{info.heading}</h1>
            <div className={styles.slider}>
                <button className={styles.left} name='left' onClick={handleBtnClick}>
                    <img src="/left.svg" alt="left" />
                </button>
                <button className={styles.right} name='right' onClick={handleBtnClick}>
                    <img src="/right.svg" alt="right" />
                </button>

                <ul ref={ulRef} style={{transform : `translateX(${pos}px)`}}>
                    {info.products.map(function(i , ind){
                        return (
                            <li key={ind}>
                                <ProductSquare info={i}/>
                            </li>
                        )
                    })}
                </ul>
            </div>
        </div>
    )
}

export default ProductSlider