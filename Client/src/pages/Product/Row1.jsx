import Details from './Details'
import Image from './Image'
import styles from './ProductPage.module.css'

function Row1({product}) {
    return (
        <div className={styles.row1}>
            <Image product={product}/>
            <Details product={product}/>
        </div>
    )
}

export default Row1