import Carousel from "./Carousel"
import Category from "./Category"
import styles from './Home.module.css'
import Row1 from "./Row1"

function Home()
{
    return (
        <div className={styles.home}>
            <Carousel/>
            <Category/>
            <Row1/>
        </div>
    )
}

export default Home