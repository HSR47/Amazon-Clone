
import styles from './ProductPage.module.css'
import Row1 from './Row1'

let product = {
    title : 'Lenovo V15 AMD Ryzen 5 5500U 15.6" (39.62cm) FHD 250 nits Antiglare Thin and Light Laptop (8GB/512GB SSD/Windows 11 Home/Iron Grey/1.7 Kg), 82KDA00XIH',
    brand : 'Lenovo',
    price : 35990,
    stars : 3.9,
    totalRatings : 193,
    description : `Processor: AMD Ryzen 5 5500U processor, base speed 2.1 Ghz, max speed 4.0 Ghz, 6 Cores, 8 MB L3 cache | Memory: 8GB DDR4 RAM 3200 MHz, upgradable up to 16 GB, Dual channel capable | Storage: 512GB SSD
    Operating System: Preloaded Windows 11 Home with Lifetime Validity
    Display: 15.6" (39.62 cm) FHD 250 nits, Antiglare, Contrast Ratio: 500:1, 90° Viewing Angle | Graphics: Integrated AMD Radeon graphics | High Definition Audio, Realtek ALC3287 codec, Stereo speakers, 1.5W x2, Dolby Audio
    Ports: 1x USB 2.0 | 1x USB 3.2 Gen 1 | 1x USB-C 3.2 Gen 1 (support data transfer only) | 1x HDMI 1.4b | 1x Ethernet (RJ-45) | 1x Headphone / microphone combo jack (3.5mm) | 1x Power connector
    Camera: 1MP with Privacy Shutter | Microphone: Dual array microphone | Keyboard: 6-row, spill-resistant, multimedia Fn keys, numeric keypad | Touchpad: Buttonless Mylar surface multi-touch touchpad, supports Precision TouchPad
    Connectivity: 802.11ac 2x2 Wi-Fi + Bluetooth 5.0 | Security: TPM 2.0 | Physical Locks: Kensington Nano Security Slot
    Battery Life: Upto 7.5 hours as per MobileMark | Integrated Li-Polymer 38Wh battery, supports Rapid Charge (charge up to 80% in 1hr) with 65W AC adapter | ENERGY STAR 8.0 Rated| Design: Thin & Light Laptop, 180 Degree Hinge
    Reliable and Durable laptop | Tests passed: Shock test, Vibration test, Hinge life test, Operating temperature test, Keyboard in-system test, Fan Reliability test, Panel scuff testand Pressure test to withstand extreme conditions
    Additional Certifications: ErP Lot 3, RoHS compliant, TÜV Rheinland Low Blue Light | This genuine Lenovo Laptop comes with 1 Year Onsite Warranty
    Inside the box: Laptop with battery, Charger, User manual`,
    images : [
        'https://m.media-amazon.com/images/I/41D+zRXM2RL.jpg',
        'https://m.media-amazon.com/images/I/61ZonMiYFzL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/51VQC6WfqQL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/61KqZczgmWL._SX679_.jpg',
        'https://m.media-amazon.com/images/I/51F2qguuw8L._SX679_.jpg',
        'https://m.media-amazon.com/images/I/616GPKWKcJL._SX679_.jpg'
    ]
}

function ProductPage(){
    return (
        <div className={styles.productPage}>
            <Row1 product={product}/>
        </div>
    )
}

export default ProductPage