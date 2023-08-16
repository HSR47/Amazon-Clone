import styles from './Home.module.css'

function Square({info}){
    
    console.log(info)
    return (
        <div className={styles.square}>
            <h1 className={styles.heading}>{info.heading}</h1>
            <ul>
                {info.products.map(function(i){
                    return (
                        <li data-goto={i.url}>
                            <img src={i.img}/>
                            <p>{i.title}</p>
                        </li>
                    )
                })}
            </ul>
            <a className={styles.seeMore} href={info.link.href}>{info.link.text}</a>
        </div>
    )
}

export default Square