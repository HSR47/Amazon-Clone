
import styles from './styles/Header.module.css'
import LeftHeader from './LeftHeader'
import MiddleHeader from './MiddleHeader'
import RightHeader from './RightHeader'
import Part2 from './Part2'
import { useEffect, useRef, useState } from 'react'

function Header() {

    let [isSticky , setIsSticky] = useState(false)
    let part1Ref = useRef(null)

    useEffect(function(){

        function handleScroll(){
            let part1Height = part1Ref.current.offsetHeight
            if (window.scrollY > part1Height)
                setIsSticky(true)
            else
                setIsSticky(false)
        }

        window.addEventListener('scroll' , handleScroll)
        return function(){
            window.removeEventListener('scroll' , handleScroll)
        }
    } , [])

    return (
        <>
            <div className={styles.header}>
                <div ref={part1Ref} className={`${styles.part1} ${isSticky ? `${styles.sticky}` : ''}`}>
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