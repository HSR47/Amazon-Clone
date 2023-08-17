import Carousel from "./Carousel"
import Category from "./Category"
import styles from './Home.module.css'
import Products from "./Products"
import Row1 from "./Row1"

function Home()
{
    return (
        <div className={styles.home}>
            <Carousel/>
            <Category/>
            <Row1/>
            <Products/>
        </div>
    )
}

export default Home