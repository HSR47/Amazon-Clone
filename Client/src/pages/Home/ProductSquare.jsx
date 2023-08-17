import { useState } from 'react'
import styles from './Home.module.css'

function ProductSquare({info}){
    let [activeImage , setActiveImage] = useState(0)

    function handleChangeImage(e){
        setActiveImage(e.target.dataset.ind)
    }

    return (
        <div className={styles.productSquare}>
            <img src={info.images[activeImage]}/>
            <p className={styles.heading}><span>{info.title}</span></p>
            <h1 className={styles.price}><span>₹</span>{info.price}</h1>
            <ul>
                {info.images.map(function(i , ind){
                    return (
                        <li key={ind}>
                            <img src={i} data-active={ind==activeImage ? 'true' : 'false'} data-ind={ind} onClick={handleChangeImage}/>
                        </li>
                    )
                })}
            </ul>
        </div>
    )
}

export default ProductSquare