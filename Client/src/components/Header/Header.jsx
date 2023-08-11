
import styles from './styles/Header.module.css'
import LeftHeader from './LeftHeader'
import MiddleHeader from './MiddleHeader'
import RightHeader from './RightHeader'
import Part2 from './Part2'

function Header() {

    return (
        <>
            <div className={styles.header}>
                <div className={styles.part1}>
                    <LeftHeader/>
                    <MiddleHeader/>
                    <RightHeader/>
                </div>

                <div className={styles.part2}>
                    <Part2/>
                </div>
            </div>
        </>
    )
}

export default Header