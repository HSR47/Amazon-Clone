import Pagination from './Pagination'
import ProductRow from './ProductRow'
import styles from './SearchPage.module.css'

let dummyproduct = {
    title : 'ASUS Vivobook Pro 15,AMD Ryzen 5 5600H,15.6" (39.62Cm) Fhd,Thin&Light Laptop (16Gb/512Gb Ssd/4Gb Nvidia Geforce RTX 3050/Windows 11/Office 2021/Backlit/Fingerprint/Blue/1.80 Kg),M6500Qc-Hn541Ws',
    stars : 4.4,
    price : 65990,
    img : 'https://m.media-amazon.com/images/I/61eTPcEsC+L._AC_UY218_.jpg'
}

let products = []

for (let i=0 ; i<16 ; i++)
{
    products.push(dummyproduct)
}


function ProductArea(){
    return (
        <div className={styles.productArea}>
            <div className={styles.heading}>Results</div>
            <div className={styles.prodContainer}>
                {products.map(function(i , ind){
                    return (
                        <ProductRow key={ind} info={i}/>
                    )
                })}
            </div>
            
            <Pagination/>
        </div>

    )
}

export default ProductArea