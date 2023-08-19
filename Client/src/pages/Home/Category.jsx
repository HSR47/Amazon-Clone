import { useEffect, useRef, useState } from 'react'
import styles from './Home.module.css'
import { useNavigate } from 'react-router-dom'

let categories = [
    {
        img : '/category/phone.jpg',
        title : 'Phone',
        slug : 'phone'
    },
    {
        img : '/category/laptop.jpg',
        title : 'Laptop',
        slug : 'laptop'
    },
    {
        img : '/category/tablet.jpg',
        title : 'Tablet',
        slug : 'tablet'
    },
    {
        img : '/category/phone.jpg',
        title : 'Phone',
        slug : 'phone'
    },
    {
        img : '/category/laptop.jpg',
        title : 'Laptop',
        slug : 'laptop'
    },
    {
        img : '/category/tablet.jpg',
        title : 'Tablet',
        slug : 'tablet'
    },
    {
        img : '/category/phone.jpg',
        title : 'Phone',
        slug : 'phone'
    },
    {
        img : '/category/laptop.jpg',
        title : 'Laptop',
        slug : 'laptop'
    },
    {
        img : '/category/tablet.jpg',
        title : 'Tablet',
        slug : 'tablet'
    },
    {
        img : '/category/phone.jpg',
        title : 'Phone',
        slug : 'phone'
    },
    {
        img : '/category/laptop.jpg',
        title : 'Laptop',
        slug : 'laptop'
    },
    {
        img : '/category/tablet.jpg',
        title : 'Tablet',
        slug : 'tablet'
    }
]

function Category(){
    let [pos , setPos] = useState(0)
    let [btnVisibility , setBtnVisibility] = useState(false)
    let navigate = useNavigate()

    let ulRef = useRef(null)
    let totalElements = categories.length

    function handleCategoryClick(e){
        let cat = e.target.closest('li')
        let url = `/products/${cat.dataset.slug}`
        navigate(url)
    }

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
            <div className={styles.slider} >
                {btnVisibility==true &&
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
                    {categories.map(function(i , ind){
                        return (
                            <li key={ind} data-slug={i.slug} onClick={handleCategoryClick}>
                                <img src={i.img}/>
                                <p>{i.title}</p>
                            </li>
                        )
                    })}
                </ul>
            </div>
        </div>
    )
}

export default Category