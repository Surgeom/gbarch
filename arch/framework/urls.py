from views import index_page, about_page,contacts_page,create_course

routes = {
    "/": index_page,
    '/about/': about_page,
    "/contacts/":contacts_page,
    "/crc/":create_course,
}
