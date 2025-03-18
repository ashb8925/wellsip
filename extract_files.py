import os
import requests

# Function to download a file
def download_file(url, folder_path):
    try:
        # Get the file name from the URL
        file_name = os.path.basename(url)
        file_path = os.path.join(folder_path, file_name)

        # Send a GET request to download the file
        response = requests.get(url, stream=True)
        response.raise_for_status()

        # Save the file
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Downloaded: {file_name}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

# Function to download all files from a list of links
def download_files_from_list(links, folder_path="downloads"):
    # Create the download folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Iterate through the list of links and download files
    for link in links:
        if link.strip():  # Skip empty links
            download_file(link, folder_path)

# Example usage
# Replace this list with the links you extracted from the console
links = [
    "https://faryita.wpengine.com/wp-content/plugins/contact-form-7/includes/css/styles.css?ver=5.9.8",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/elementor/assets/css/elementor.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/assets/css/common.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/assets/css/widget.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/assets/css/core.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce/assets/css/woocommerce-layout.css?ver=9.1.4",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce/assets/css/woocommerce-smallscreen.css?ver=9.1.4",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce/assets/css/woocommerce.css?ver=9.1.4",
    "https://faryita.wpengine.com/wp-content/plugins/yith-woocommerce-compare/assets/css/colorbox.css?ver=1.4.21",
    "https://faryita.wpengine.com/wp-content/plugins/yith-woocommerce-quick-view/assets/css/yith-quick-view.css?ver=1.41.0",
    "https://faryita.wpengine.com/wp-content/plugins/ti-woocommerce-wishlist/assets/css/webfont.min.css?ver=2.8.2",
    "https://faryita.wpengine.com/wp-content/plugins/ti-woocommerce-wishlist/assets/css/public.min.css?ver=2.8.2",
    "https://faryita.wpengine.com/wp-content/plugins/elementor/assets/lib/swiper/v8/css/swiper.min.css?ver=8.4.5",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/all.min.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/material-design-iconic-font.min.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/base.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/common.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/modules-listing.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/modules-default.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/custom-frontend-lite.min.css?ver=1733978987",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-17.css?ver=1733978987",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/global.css?ver=1733978989",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-285.css?ver=1733982908",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/social-share/assets/social-share-frontend.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/chosen.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/fields.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/search/assets/search-frontend.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/media-images/assets/media-images-frontend.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/media-attachments/assets/media-attachments-frontend.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/assets/css/modules-singlepage.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/comments/assets/comments-frontend.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-portfolio/modules/business-hours/assets/business-hours-frontend.css?ver=6.7.1",
    "https://fonts.googleapis.com/css?family=Anton:+400&subset=latin-ext",
    "https://fonts.googleapis.com/css?family=Just+Another+Hand:+400&subset=latin-ext",
    "https://fonts.googleapis.com/css?family=Outfit:100,200,300,400,500,600,700,800,900&subset=latin-ext",
    "https://fonts.googleapis.com/css?family=Poppins:+100,+100italic,+200,+200italic,+300,+300italic,+regular,+italic,+500,+500italic,+600,+600italic,+700,+700italic,+800,+800italic,+900,+900italic&subset=latin-ext",
    "https://faryita.wpengine.com/wp-content/themes/faryita/style.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/icons.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/base.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/grid.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/layout.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/widget.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/classic.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/breadcrumb/assets/css/breadcrumb.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/header/assets/css/header.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/site-loader/layouts/loader-3/assets/css/loader-3.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/site-to-top/assets/css/totop.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/sidebar/assets/css/sidebar.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/blog/assets/css/blog.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/blog/templates/minimal/assets/css/blog-archive-minimal.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/blog/assets/css/jquery.bxslider.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/breadcrumb/assets/css/breadcrumb.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/comments/assets/css/comments.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/footer/assets/css/footer.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/header/assets/css/header.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/pagination/assets/css/pagination.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/post/assets/css/magnific-popup.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/search/assets/css/search.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/sidebar/assets/css/sidebar.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/woocommerce/assets/css/default.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/blog/assets/css/blog.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/menu/assets/css/nav-menu-animations.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/menu/assets/css/nav-menu.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/advance-field/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/blog/assets/css/blog.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/post/assets/css/post-navigation.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/auth/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/lib/select2/select2.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/themes/faryita/assets/css/theme.css?ver=1.0.2",
    "https://fonts.googleapis.com/css?family=Anton%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic%7CPoppins%3A100%2C100italic%2C200%2C200italic%2C300%2C300italic%2C400%2C400italic%2C500%2C500italic%2C600%2C600italic%2C700%2C700italic%2C800%2C800italic%2C900%2C900italic&display=swap&ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce/assets/client/blocks/wc-blocks.css?ver=wc-9.1.4",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce-currency-switcher/js/chosen/chosen.min.css?ver=1.4.2",
    "https://faryita.wpengine.com/wp-content/plugins/woocommerce-currency-switcher/css/front.css?ver=1.4.2",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/custom-widget-icon-list.min.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-383.css?ver=1733978990",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/menu/elementor/widgets/assets/css/logo.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/menu/elementor/widgets/assets/css/header-icons.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/menu/elementor/widgets/assets/css/header-carticon.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/button/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-387.css?ver=1733982908",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-353.css?ver=1733982908",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/heading/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/common-controls/repeater-contents/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/image-box/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/image-box/assets/css/jquery.magnific-popup.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-676.css?ver=1733982908",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-675.css?ver=1733982908",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/common-controls/layout/assets/css/swiper.min.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/common-controls/layout/assets/css/carousel.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/advanced-carousel/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/common-controls/layout/assets/css/column.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/animation/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/woocommerce/listings/elementor/widgets/products/assets/css/swiper.min.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/woocommerce/assets/css/carousel.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-pro/modules/woocommerce/listings/elementor/widgets/products/assets/css/style.css?ver=6.7.1",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/icon-box/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/accordion-and-toggle/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/team/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/themes/faryita/modules/blog/templates/simple/assets/css/blog-archive-simple.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/plugins/faryita-plus/modules/blog/elementor/widgets/assets/css/blogcarousel.css?ver=1.0.2",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-255.css?ver=1733978991",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/widgets/mailchimp/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-270.css?ver=1733978992",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-510.css?ver=1733978992",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-511.css?ver=1733978992",
    "https://faryita.wpengine.com/wp-content/uploads/elementor/css/post-365.css?ver=1733980494",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/core/sections/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/core/columns/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/inc/core/widgets/assets/css/style.css?ver=1.0.0",
    "https://faryita.wpengine.com/wp-content/plugins/wedesigntech-elementor-addon/assets/css/animations.min.css?ver=1.0.0"
]

# Download files from the list
download_files_from_list(links)