import Service from '@ember/service';

export default class ApiService extends Service {
  host = '';        // use same domain as the page
  namespace = '/api';

  async request(path, options = {}) {
    const res = await fetch(`${this.host}${this.namespace}${path}`, {
      headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
      ...options,
    });
    if (res.status === 204) return null;
    const text = await res.text();
    if (!res.ok) throw new Error(text || `HTTP ${res.status}`);
    try { return JSON.parse(text); } catch { return text; }
  }

  getTasks() { return this.request('/tasks/'); }
  createTask(payload) { return this.request('/tasks/', { method: 'POST', body: JSON.stringify(payload) }); }
  updateTask(id, payload) { return this.request(`/tasks/${id}/`, { method: 'PUT', body: JSON.stringify(payload) }); }
  deleteTask(id) { return this.request(`/tasks/${id}/`, { method: 'DELETE' }); }
}
