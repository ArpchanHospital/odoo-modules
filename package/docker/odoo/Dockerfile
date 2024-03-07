FROM odoo:10

ENV ADDON_PATH=/opt/bahmni-erp/bahmni-addons
COPY package/docker/odoo/odoo.conf /etc/odoo/odoo.conf
COPY bahmni_account ${ADDON_PATH}/bahmni_account/
COPY bahmni_atom_feed ${ADDON_PATH}/bahmni_atom_feed/
COPY bahmni_product ${ADDON_PATH}/bahmni_product/
COPY bahmni_purchase ${ADDON_PATH}/bahmni_purchase/
COPY bahmni_sale ${ADDON_PATH}/bahmni_sale/
COPY bahmni_stock ${ADDON_PATH}/bahmni_stock/
COPY bahmni_web_extension ${ADDON_PATH}/bahmni_web_extension/
COPY web_readonly_bypass ${ADDON_PATH}/web_readonly_bypass/
COPY todo_app ${ADDON_PATH}/todo_app/
COPY testodoo-main ${ADDON_PATH}/testodoo-main/
COPY report_csv ${ADDON_PATH}/report_csv/
COPY purchase_discount ${ADDON_PATH}/purchase_discount/
COPY account_financial_report_qweb ${ADDON_PATH}/account_financial_report_qweb/
COPY account_group ${ADDON_PATH}/account_group/
COPY date_range ${ADDON_PATH}/date_range/
COPY report_xlsx ${ADDON_PATH}/report_xlsx/
COPY web_widget_many2many_tags_multi_selection ${ADDON_PATH}/web_widget_many2many_tags_multi_selection/
COPY report_pdf_options ${ADDON_PATH}/report_pdf_options/
COPY web_pdf_preview ${ADDON_PATH}/web_pdf_preview/
# COPY account_report_xlsx_menu ${ADDON_PATH}/account_report_xlsx_menu/
CMD ["odoo", "-u", "all"]
# Install debugpy for remote debugging
RUN pip3 install debugpy

# Use a shell command to check the ODOO_DEBUG_MODE environment variable
CMD if [ "$ODOO_DEBUG_MODE" = "true" ]; then \
        echo "Starting Odoo in debug mode..."; \
        exec python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client /usr/bin/odoo -u all -c /etc/odoo/odoo.conf; \
    else \
        echo "Starting Odoo normally..."; \
        exec /usr/bin/odoo -u all -c /etc/odoo/odoo.conf; \
    fi
