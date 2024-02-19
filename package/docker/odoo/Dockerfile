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
CMD ["odoo", "-u", "all"]
