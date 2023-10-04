import styles from './ProductPage.module.css'
import { useState } from 'react'


function Image({ product }) {
    let [activeImg, setActiveImg] = useState(0)

    function handleImgClick(e){
        setActiveImg(e.target.dataset.index)
    }
    return (
        <div className={styles.image}>
            <div className={styles.container}>
                <ul>
                    {product.images.map(function (i, ind) {
                        return (
                            <li key={ind}>
                                <img data-index={ind} src={i} onMouseEnter={handleImgClick}/>
                            </li>
                        )
                    })}
                </ul>

                <div className={styles.active}>
                    <img src={product.images[activeImg]} />
                </div>
            </div>
        </div>
    )
}

export default Image